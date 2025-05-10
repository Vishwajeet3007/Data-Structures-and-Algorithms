class Process:
    def __init__(self, pid):
        self.pid = pid
        self.allocated = {}
        self.requested = {}

    def allocate_resource(self, resource, amount):
        if resource in self.requested and self.requested[resource] >= amount:
            self.allocated[resource] = amount
            self.requested[resource] -= amount
            return True
        return False

    def release_resource(self, resource, amount):
        if resource in self.allocated and self.allocated[resource] >= amount:
            self.allocated[resource] -= amount
            return True
        return False

    def request_resource(self, resource, amount):
        self.requested[resource] = amount

class Resource:
    def __init__(self, rid):
        self.rid = rid
        self.total = 0

    def set_total(self, amount):
        self.total = amount

def build_rag(processes):
    rag = {}
    for process in processes:
        for resource, amount in process.requested.items():
            if amount > 0:
                if resource not in rag:
                    rag[resource] = set()
                rag[resource].add(process.pid)
    return rag

# Example usage
if __name__ == "__main__":
    # Create processes
    p1 = Process(1)
    p2 = Process(2)
    p3 = Process(3)

    # Create resources
    r1 = Resource('R1')
    r2 = Resource('R2')

    # Set total resources
    r1.set_total(3)
    r2.set_total(2)

    # Allocate resources to processes
    p1.allocate_resource(r1.rid, 1)
    p2.allocate_resource(r1.rid, 2)
    p3.allocate_resource(r2.rid, 1)

    # Request resources
    p1.request_resource(r2.rid, 1)
    p2.request_resource(r2.rid, 1)

    # Build Resource Allocation Graph
    processes = [p1, p2, p3]
    rag = build_rag(processes)

    # Print Resource Allocation Graph
    print("Resource Allocation Graph:")
    for resource, processes in rag.items():
        print(f"{resource}: {', '.join(str(pid) for pid in processes)}")
