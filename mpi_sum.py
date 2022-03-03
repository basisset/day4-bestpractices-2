from mpi4py import MPI
import os

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
rank_sum = 0

if rank != 0:
    req = comm.send(rank, dest=0, tag=11)

elif rank == 0:
    for i in range(1,size):
        rank_sum += comm.recv(source=i, tag=11)
    print(f"Sum of ranks is {rank_sum}")

