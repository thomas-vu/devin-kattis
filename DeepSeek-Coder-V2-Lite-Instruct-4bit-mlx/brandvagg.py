class Firewall:
    def __init__(self, rules):
        self.rules = []
        for rule in rules:
            parts = rule.split()
            condition = {}
            action = 'accept' if parts[1] == 'accept' else ('log' if parts[1] == 'log' else 'drop')
            for part in parts[2:]:
                key, value = part.split('=')
                condition[key] = value
            self.rules.append((condition, action))

    def process_packet(self, packet):
        ip, port = packet.split(':')
        for condition, action in self.rules:
            if 'port' in condition and int(condition['port']) != int(port):
                continue
            if 'ip' in condition and condition['ip'] != ip:
                continue
            if 'limit' in condition:
                limit = int(condition['limit'])
                # This is a placeholder for the logic to check the limit condition
                # For now, let's assume we have a method to keep track of the last 1000 messages
                # which is not implemented yet.
                pass
            if action == 'accept':
                print(f"accept {packet_id}")
                return True
            elif action == 'log':
                print(f"log {packet_id}")
                return True
            elif action == 'drop':
                print(f"drop {packet_id}")
                return False
        return False

# Main function to process the input and output accordingly
def main():
    n = int(input())
    rules = [input().strip() for _ in range(n)]
    m = int(input())
    packets = [input().strip() for _ in range(m)]
    
    firewall = Firewall(rules)
    for packet_id, packet in enumerate(packets, start=1):
        if not firewall.process_packet(packet):
            break

if __name__ == "__main__":
    main()