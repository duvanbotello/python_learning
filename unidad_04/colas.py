from collections import deque

#manejando colas con python

cola = deque(['Duvan','Carlos','Sebastian'])
cola.append('maria')
cola.popleft()
print(cola)
