import os

def get_max_weight(path: str):

    if os.path.isfile(path):
        weights = []
        
        with open(path, 'r') as f:
            
            package_w = 0
            for line in f:
                if line.strip():
                    package_w += int(line)
                else:
                    weights.append(package_w)
                    package_w = 0
    else:
        raise ValueError('File does`t exists')
    
    with open('./baliky.txt', 'w') as fp:
        for i, item in enumerate(weights, start=1):
            fp.write(f'Balík {i}: {item} kg\n')
    
    max_idx = weights.index(max(weights))
    
    return max_idx, weights[max_idx]

if __name__ == '__main__':
    idx, value = get_max_weight('./veci.txt')
    print(f'Maximální hmotnost {value} kg má balík číslo {idx + 1}')