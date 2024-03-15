#Single Beam Calculator

l = float(input("Beam length: ")) #length in m
q = []
a_q = []
l_q = []
P = []
a_P = []
n_q = int(input("Number of distributed loads: "))
if n_q>0:
    for i in range(n_q):
        q.append(float(input("Distributed load: ")))#distributed load in kN
        a_q.append(float(input("Distributed load's starting position from left: "))) #starting position of load q in m
        l_q.append(float(input("Distributed load's total length: "))) #length of distributed load q in m

n_P = int(input("Number of single loads: "))
if n_P>0:
    for i in range(n_P):
        P.append(float(input("Single load Nr." + str(i+1)+": ")))
        a_P.append(float(input("Single load's Nr."+str(i+1)+" starting position from left: ")))
P_sum = 0
B_P = 0
for i in range(n_P):
    B_P += P[i]*a_P[i]/l  #Reaction force B (right side) due to single load P
    P_sum += P[i]
q_sum = 0
B_q = 0
for i in range(n_q):
    B_q += q[i]*l_q[i]*(a_q[i]+l_q[i]/2)/l
    q_sum += q[i]*l_q[i]
    
B = B_P+B_q
A_P = P_sum - B_P
A_q = q_sum - B_q

A = A_P +A_q

print("Α,P= "+str(A_P)+"kN","B,P= "+str(B_P)+"kN")

print("Α,q= "+str(A_q)+"kN","B,q= "+str(B_q)+"kN")

print("A,tot = "+str(A)+"kN ,Btot= "+str(B)+"kN")



