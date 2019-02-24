import numpy as np
import math
import random
class Chromosome:
    """
    Loi giai bai toan la arr kich thuoc bang so luong sensor, day la vi tri cua sensor
    Note:
    1: num_targets = n, num_sensors = m. solution = []*m
    2: Constraint: - Coverage: _check_coverage(arr_tar,solution)
                   
    
    """
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness
def _check_movement(So):
    """
    params : So - mang solution luu mot loi giai cua bai toan duoi dang So = [[0,0,0,1...]] kich thuoc m*k1
    ---------------------------------------------------------------------------------------------------------------
    check: cong theo cot matrix solution dc am tran mx1. cac phan tu cot <= 1
    """
    _check = [] 
    for row in So:
        val_col = 0
        for val in row:
            val_col += val
            _check.append(val_col)
    for val in _check:
        if val > 1:
            return False
    return True
    
    
        

def _check_coverage(LoT,So,LS):
    """
    params: 
        arr_tar: mang target can duoc bao phu
        solution: mang cac index cua mang vi tri sensors co the
    output: 
        return True if Coverage
    note: 
        - mang target lay trong setOfPoints. duoc luu duoi dang T = [[target1_x,target1_y],[target2_x,target2_y]]
        - mang vi tri cac sensor co the toi duoc luu duoi dang LS = [[sensor1_1,sensor1_2,..],[sensor2_1,...]] kich thuoc mxk1 vs k1 > n
        - mang solution luu mot loi giai cua bai toan duoi dang So = [[0,0,0,1...]] kich thuoc m*k1
        - mang cac diem kha dung cua mot target: LoT = [[target1_1,target1_2,...]] , kich thuoc la n*k2 vs k2 > m Cac diem nay cung la cac phan tu trong mang L
        - Check : 
                + cac vi tri ay phai bao phu het sensor:  
    
        
    """
    _is_covered_targets = [0]*n
    for j in range(len(So)):
        index = So[j].index(1)
        for i in range(len(LoT)):
            if _is_covered_targets[i] == 0 and LS[j][index] in LoT[i]: #doan nay co the co bug
                _is_covered_targets[i] = 1
                break
    return 0 in _is_covered_targets

def _get_distances(solution,Sensors,LS):
    """
    params: 
        Sensors:
            + type: array<Point>
        solution: 
            + array<int><int>
        LS:
            + array<Point>
    output:
        return 1 tuple d(dMin,dMax), trong do d[0] la khoang cach di chuyen nho nhat cua sensor, d[1] la max

    """

    dist_arr = []
    for i in range(len(solution)):
        for j in range(len(solution)):
            if solution[i][j] == 1:
                squareD = Sensors[i]._get_square_distance(LS[i][j])
                dis_arr.append(math.sqrt(squareD))
                break
            dist_arr.append(0)
    sorted_index = np.argsort(dist_arr)
    dMax = dist_arr[sorted_index[-1]]
    dMin = dist_arr[sorted_index[0]]
    return (dMin,dMax)

def _generate_parent(num_rows,num_cols,LoT,So,LS):
    """
    Sinh ra ngau nhien mot mang cac phan tu 0,1 goi la RG[[]]
    Sau do check hai dieu kien bao phu va di chuyen
        
    """
    # RG = [[0]*num_cols]*num_rows
    RG = []
    _is_solution = False
    while _is_solution == False:
        RG += [[0]*num_cols]*num_rows
        for i in num_rows:
            index = random.randint(0,num_cols-1)
            RG[i][index] = 1
        _is_solution = _check_movement(RG) and _check_coverage(LoT,RG,LS)
    
    return RG

def is_dominated(So1,So2,Sensors,LS):
    """
    Solution1 troi hon Solution2 theo mat tap cac objects thi phai thoa man, tat cac object cua So1 tot hon hoac bang So2 va it nhat mot cai tot hon. 
    """
    d1 = _get_distances(So1,Sensors,LS)
    d2 = _get_distances(So1,Sensors,LS)
    return d1[0] > d2[0] and d1[1] >= d2[1] or d1[0] >= d2[0] and d1[1] > d2[1]

def fast_none_dominated_sort(P,Sensors,LS):
    """
    Meaning: Thu hien sap xep khong troi, cac solution trong P se duoc xep vao cac rank cua no
    --------------------------------------------------------------------
    Input: 1 tap cac solution goi la P 
    --------------------------------------------------------------------
    Output
    --------------------------------------------------------------------
    Note: Doan xac dinh index cua q,q co the xay ra bug, do cac sol trong P chua dc kiem tra doi mot khac nhau. 
    """
    F = [[]]
    S = [[]]*len(P)
    n = [0]*len(P)
    rank = [1]* len(P)
    for index_p in range(len(P)):
        for index_q in range(len(P)):
            if is_dominated(P[index_p],P[index_q],Sensors,LS) == True:
                S[index_p].append(P[index_q])
            elif is_dominated(P[index_q],P[index_p],Sensors,LS) == True:
                n[index_p] += 1
        if n[index_p] == 0:
            rank[index_p] = 1
            F[0].append(p)

            
    i = 1
    temp_Fi = F[i-1]
    while len(temp_Fi) > 0:
        Q = []
        for p in temp_Fi:
            index_p = P.index(p)
            for q in S[index_p]:
                index_q = P.index(q)
                n[index_q] -= 1
                if n[index_q] == 0:
                    rank[index_q] = i+1
                    Q.append(q)
        i += 1
        temp_Fi = Q
        F.append(temp_Fi)
    return F

def mutate(solution,mutation_rate):
    for swapped in range(len(solution)):
        if random.random()< mutation_rate:
            swap_with = int(random.random()*len(solution))
            pos1 = solution[swapped]
            pos2 = solution[swap_with]
            solution[swapped] = pos2
            solution[swap_with] = pos1
    return solution

def mutate_population(solutions,mutation_rate):
    mutatedPop = []
    for ind in range(len(solutions)):
        mutatedInd = mutate(solutions[ind],mutation_rate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

def crossover(solution1,solution2):
    randIndex1 = int(random.random()*len(solution1))
    randIndex2 = int(random.random()*len(solution1))
    startGene = min(randIndex1,randIndex2)
    endGene = max(randIndex1,randIndex2)

    childP1 = [item for item in solution1[0:randIndex1]]
    childP2 = [item for item in solution2[randIndex1:randIndex2]]
    childP3 = [item for item in solution1[randIndex2:]]
    return childP1+childP2+childP3

def select_parrents(P,Sensors,LS,num_parrents):
    """
    select the fittest individuals to be parents of next generation: call "fast_none_dominated_sort" and then get "num_parrents"-10 individuals from rank 1. 
    also select a some random non-fittest individuals to help us get out of local optimization
    """
    F = fast_none_dominated_sort(P,Sensors,LS)
    parents1 = []
    n = 0
    while n < num_parrents-10:
        for Fi in F:
            if len(Fi) > 0:
                for k in Fi:
                    parents1.append(k)
                    n+=1
    parents2 = []
    while len(parents2) < 10:
        item = random.choice(P)
        if item not in parents1 and item not in parents2:
            parents2.append(item)
    
    return parents1+parents2

def crossover_pop(P,Sensors,LS,num_parrents):
    target_children_size = len(P) - num_parrents
    parents = select_parrents(P,Sensors,LS,num_parrents)
    children = []
    if len(num_parrents)>0:
        while len(children) < target_children_size:
            father = random.choice(parents)
            mother = random.choice(parents)
            if father!= mother:
                child = crossover(father,mother)
                children.append(child)
    P = parents + children


def GA(P,Sensors,LS,num_parrents,max_generation,mutatation_rate):
    for i in range(max_generation):
        crossover_pop(P,Sensors,LS,num_parrents)
        mutate_population(P,Sensors,mutatation_rate)
    best = fast_none_dominated_sort(P,Sensors,LS)[0]
    



    

        










    

        

