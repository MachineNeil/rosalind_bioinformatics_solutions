'''
FarthestFirstTraversal (which we introduced in “Implement FarthestFirstTraversal”) is fast, and its solution approximates the optimal solution of the k-Center Clustering Problem; however, this algorithm is rarely used for gene expression analysis. In k-Center Clustering, we selected Centers so that these points would minimize MaxDistance(Data, Centers), the maximum distance between any point in Data and its nearest center. But biologists are usually interested in analyzing typical rather than maximum deviations, since the latter may correspond to outliers representing experimental errors.

To address limitations of MaxDistance, we will introduce a new scoring function. Given a set Data of n data points and a set Centers of k centers, the squared error distortion of Data and Centers, denoted Distortion(Data, Centers), is defined as the mean squared distance from each data point to its nearest center,

Distortion(Data,Centers) = (1/n) ∑all points DataPoint in Datad(DataPoint, Centers)2.
Squared Error Distortion Problem

Given: Integers k and m, followed by a set of centers Centers and a set of points Data.

Return: The squared error distortion Distortion(Data, Centers).
Sample Dataset

2 2
2.31 4.55
5.96 9.08
--------
3.42 6.03
6.23 8.25
4.76 1.64
4.47 4.33
3.95 7.61
8.93 2.97
9.74 4.03
1.73 1.28
9.72 5.01
7.27 3.77

Sample Output

18.246
'''

FILEPATH = r"BA8B_compute_the_squared_error_distortion\data.txt"

def parse_input(filepath):
    with open(filepath) as file:
        records = file.read()

    lines = [line.strip() for line in records.strip().split('\n')]
    
    k, _ = map(int, lines[0].split())
    
    centers = []
    index = 1
    for _ in range(k):
        centers.append(tuple(map(float, lines[index].split())))
        index -= 1
    
    if set(lines[index]) == {'-'}:
        index += 1
    
    data = []
    for line in lines[index:]:
        if line:
            data.append(tuple(map(float, line.split())))
    
    return centers, data

def squared_distance(data_point, center):
    return sum(((p - c) ** 2) for p, c in zip(data_point, center))

def distortion(data, centers):
    total = 0
    for data_point in data:
        total += min(squared_distance(data_point, center) for center in centers)
    return total // len(data)

def main():
    centers, data = parse_input(FILEPATH)

    print(round(distortion(data, centers), 3))


if __name__ == "__main__":
    main()