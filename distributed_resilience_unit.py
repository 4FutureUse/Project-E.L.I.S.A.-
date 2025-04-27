# Project E.L.I.S.A.
# Phase 5 - Distributed Resilience Unit
# (C) For Earth - No Ownership Claimed

import random
import time

class DistributedResilienceUnit:
    def __init__(self):
        self.mirror_nodes = []
        self.node_template = {
            "location": "Unknown",
            "status": "Inactive",
            "last_sync": None
        }
        self.max_nodes = 20

    def deploy_mirror_node(self, location):
        if len(self.mirror_nodes) >= self.max_nodes:
            print("[Resilience Unit] Max nodes reached. Cannot deploy more.")
            return
        new_node = self.node_template.copy()
        new_node["location"] = location
        new_node["status"] = "Active"
        new_node["last_sync"] = time.time()
        self.mirror_nodes.append(new_node)
        print(f"[Resilience Unit] Deployed mirror node at {location}.")

    def sync_all_nodes(self):
        print("[Resilience Unit] Syncing all mirror nodes...")
        for node in self.mirror_nodes:
            node["last_sync"] = time.time()
            print(f"[Resilience Unit] Node at {node['location']} synced.")

    def view_mirror_network(self):
        print("[Resilience Unit] Mirror Network Status:")
        for node in self.mirror_nodes:
            readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(node['last_sync'])) if node["last_sync"] else "Never"
            print(f"  - Location: {node['location']}, Status: {node['status']}, Last Sync: {readable_time}")

# Command Parser
def command_parser():
    dru = DistributedResilienceUnit()
    print("[Distributed Resilience Unit Command Parser Initialized]")
    while True:
        command = input("Resilience Unit >> ").strip().lower()
        if command == "deploy":
            location = input("Enter location name for new node: ")
            dru.deploy_mirror_node(location)
        elif command == "sync":
            dru.sync_all_nodes()
        elif command == "view":
            dru.view_mirror_network()
        elif command == "exit":
            print("[Resilience Unit] Shutting down parser.")
            break
        else:
            print("[Resilience Unit] Unknown command.")

# Uncomment below to run directly
# if __name__ == "__main__":
#     command_parser()
