#roulette wheel algorithm 
import random
def roulette_wheel_select(prob_array):
    total_prob = sum(prob_array)
    random_prob =random.uniform(0,total_prob)
    current=0
    
    for i, prob in enumerate(prob_array):
        current+=prob 
        if current>random_prob:
            return i
import numpy as np
import math
#initialization of variables
ants= 5
areas= 5
iterations= 10
alpha= 0.5
beta= 0.5
#areas graph
distance= np.random.randint(1,50,size=(areas,areas))
#convert to symmetric
distance= (distance + distance.T)/2
distance= distance.astype(int)
for i in range(0,areas):
    distance[i,i]=0
#pheromones graph
pheromone= np.ones((areas,areas))
best_one_route=[]
best_one_distance=[]
for iteration in range(iterations):
    pheromone_sum=np.zeros((areas,areas))
    #placing ants to random areas
    ant_areas = [[random.randint(0, areas-1)] for ant in range(ants)]
    for ant in ant_areas:
        while len(ant) < areas:
            #starting area of each ant
            area=ant[-1]
            available_areas=[a for a in range(areas) if a not in ant] 
            #calculating the desire of the ant choosing each path
            probabilities=[(pheromone[area][a] ** alpha)*(1/distance[area][a]  ** beta) for a in available_areas]
            #calculating the sum of all desires
            total_pheromone=sum(probabilities)
            probabilities=[prob/total_pheromone for prob in probabilities]
            #choosing next path using roulette wheel selection
            next_area=available_areas[roulette_wheel_select(probabilities)]
            pheromone_sum[area][next_area] = 0.5*pheromone_sum[area][next_area]+1/distance[area][next_area]
            pheromone_sum[next_area][area] = 0.5*pheromone_sum[next_area][area]+1/distance[next_area][area]
            ant.append(next_area)
    #distance sum of the route each ant have chosen
    ant_distances=[]
    for ant in ant_areas:
        this_distance=0
        for i in range(len(ant)-1):
            this_distance += distance[ant[i]][ant[i+1]]
        ant_distances.append(this_distance)
    
    #returning each ant to its original area
    for i in range(len(ant_areas)):
        ant_distances[i] += distance[ant_areas[i][0]][ant_areas[i][4]]
        ant_areas[i].append(ant_areas[i][0])
    
    #the best route of all the chosen ones
    best_route=ant_areas[ant_distances.index(min(ant_distances))]
    best_one_route.append(best_route)
    best_one_distance.append(min(ant_distances))
    #updating pheromones
    for i in range(areas):
        for j in range(areas):
            if i!=j:
                pheromone[i][j] = 0.5*pheromone[i][j]+pheromone_sum[i][j] #evaporation rate=0.5
print("\nbest route after ", iteration+1, " iterations:", min(best_one_route), "with distance (cost) summation:", min(best_one_distance),"\n")