import sys

def process_events(car_types, events):
    spy_data = {}
    
    for event in events:
        time, spy, e_type, *details = event
        
        if spy not in spy_data:
            spy_data[spy] = {'current_car': None, 'total_cost': 0}
        
        if e_type == 'p' and details:
            car_name = details[0]
            if car_name not in car_types:
                return "INCONSISTENT"
            spy_data[spy]['current_car'] = car_name
            spy_data[spy]['total_cost'] += car_types[car_name]['pickup_cost']
        
        elif e_type == 'r' and details:
            distance = details[0]
            if spy_data[spy]['current_car'] is None:
                return "INCONSISTENT"
            cost_per_km = car_types[spy_data[spy]['current_car']]['cost_per_km']
            spy_data[spy]['total_cost'] += distance * cost_per_km
            spy_data[spy]['current_car'] = None
        
        elif e_type == 'a' and details:
            severity = details[0]
            if spy_data[spy]['current_car'] is None:
                return "INCONSISTENT"
            car_cost = car_types[spy_data[spy]['current_car']]['catalog_price']
            repair_cost = (severity / 100) * car_cost
            spy_data[spy]['total_cost'] += repair_cost
    
    return spy_data

def main():
    input_lines = sys.stdin.read().splitlines()
    num_test_cases = int(input_lines[0])
    
    for i in range(1, num_test_cases + 1):
        n, m = map(int, input_lines[i].split())
        car_types = {}
        
        for _ in range(n):
            line = input_lines[i + 1]
            name, catalog_price, pickup_cost, cost_per_km = line.split()
            car_types[name] = {
                'catalog_price': int(catalog_price),
                'pickup_cost': int(pickup_cost),
                'cost_per_km': int(cost_per_km)
            }
        
        events = []
        for _ in range(m):
            line = input_lines[i + 1 + n + _]
            t, S, e, *details = line.split()
            events.append((int(t), S, e, *details))
        
        spy_data = process_events(car_types, events)
        
        for spy in sorted(spy_data.keys()):
            total_cost = spy_data[spy]['total_cost']
            print(f"{spy} {total_cost if total_cost != 'INCONSISTENT' else 'INCONSISTENT'}")
        
        i += n + m

if __name__ == "__main__":
    main()