from tqdm import tqdm

sum_ = 0

# trange = tqdm(range(100), ncols=80, desc='hello', unit='epoch')
# возвращает тот же список range(100)

# можно задать свой формат вывода
my_bar = '| {n_fmt}/{total_fmt} [{elapsed}<{remaining}] loss=0.3'
trange = tqdm(range(100), bar_format='{l_bar}{bar}'+my_bar)

    
for i in trange:
    # теперь будет progress bar
    sum_ += i
    
    # на ходу можно менять описание (слева)
    # trange.set_description('It-{}'.format(i))
    
    # можно добавить доп инфу в конец
    # trange.set_postfix(loss=3, gen=34, lst=['a', 'b'])
    
# можно менять самому менять шаг
with tqdm(total=100, desc='hello2') as pbar:
    for i in range(10):
        sum_ += i
        pbar.update(10)  # следи, чтобы не вышло за пределы total
        # pbar.update()    # до конца
        
# или вместо with .. as используй pbar.close()
# print(sum_)