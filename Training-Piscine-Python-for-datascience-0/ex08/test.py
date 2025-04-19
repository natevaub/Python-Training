from time import sleep
from tqdm import tqdm
# from Loading import ft_tqdm


def ft_tqdm(lst: range):
    total = len(lst)
    counter = 0
    
    for i in lst:
        counter += 1
        progress = int(counter * 50 / total)
        percentage = int(counter * 100 / total)
        
        print(f"\r{counter}/{total} [{('='*progress)}{' '*(50-progress)}] {percentage}%", end='')
        yield i

for elem in ft_tqdm(range(333)): 
    sleep(0.005)


for elem in tqdm(range(333)):
    sleep(0.005)

print()