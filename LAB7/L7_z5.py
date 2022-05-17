import matplotlib.pyplot as plt
import multiprocessing as mp
import numpy as np


size = 20
INTERVAL = 0.5
L = np.random.randint(0, 100, size)
X = np.arange(size)

def heap_sort_global(l):
    def heapify(arr, n, i):
        largest = i # Ustawienie największego jako ojciec
        l = 2 * i + 1	 # lewy syn = 2*i + 1
        r = 2 * i + 2	 # prawy syn = 2*i + 2

        # Sprwdzamy czy lewy syn istnieje
        # i jest większy od ojca
        if l < n and arr[largest] < arr[l]:
            largest = l

        # Sprwdzamy czy prawy syn istnieje
        # i jest większy od ojca
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Zmiana ojca jeśli spełniony jest warunek
        if largest != i:
            
            arr[i], arr[largest] = arr[largest], arr[i] # swap

            plt.bar(X, arr)
            plt.title('Sortowanie przez kopcowanie')
            plt.pause(INTERVAL)
            plt.clf()


            # ponowne wywołanie kopcowania
            heapify(arr, n, largest)


    def heapSort(arr):
        n = len(arr)

        # Budowanie największego kopca
        for i in range(n//2 - 1, -1, -1):
            heapify(arr, n, i)

        # ektrakcja elementów
        for i in range(n-1, 0, -1):

            arr[i], arr[0] = arr[0], arr[i] # zamiana

            plt.bar(X, arr)
            plt.title('Sortowanie przez kopcowanie')
            plt.pause(INTERVAL)
            plt.clf()

            heapify(arr, i, 0)

    heapSort(l)



def quic_sort_global(l):
    def quick_sort(arr, low, high):
        if low > high: # or high >= len(arr):
            return
        
        p, arr =  partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

        return arr


    def partition(arr, low, high):
        piv = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] <= piv:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]

                plt.bar(X, arr)
                plt.title('Quicksort - sortowanie szybkie')
                plt.pause(INTERVAL)
                plt.clf()
        
        i += 1
        arr[i], arr[high] = arr[high], arr[i]

        plt.bar(X, arr)
        plt.title('Quicksort - sortowanie szybkie')
        plt.pause(INTERVAL)
        plt.clf()
        
        return i, arr

    quick_sort(l, 0, len(l) - 1)


if __name__ == '__main__':
    
    task1 = mp.Process(target=heap_sort_global, args=(L,))
    task2 = mp.Process(target=quic_sort_global, args=(L,))

    task1.start()
    task2.start()

    plt.show()