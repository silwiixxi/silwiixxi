#601
n=int(input())
print(sum(map(lambda x:int(x)**2,input().split())))

#602
n=int(input())
print(len(list(filter(lambda x:int(x)%2==0,input().split()))))

#603
n=int(input())
print(*[f"{i}:{w}" for i,w in enumerate(input().split())])

#604
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(sum(x*y for x,y in zip(a,b)))

#605
s=input()
print("Yes"if any(c in"aeiouAEIOU"for c in s)else"No")

#606
n=int(input())
print("Yes"if all(int(x)>=0 for x in input().split())else"No")

#607
n=int(input())
print(max(input().split(),key=len))

#608
n=int(input())
print(*sorted(set(map(int,input().split()))))

#609
n=int(input())
d=dict(zip(input().split(),input().split()))
q=input()
print(d.get(q,"Not found"))

#610
n=int(input())
print(sum(map(bool,map(int,input().split()))))
