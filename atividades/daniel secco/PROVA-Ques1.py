nums = []

for i in range(5):
    num = int(input("Digite um número: "))
    nums.append(num)


soma = 0
maior = nums[0]
menor = nums[0]

for num in nums:
    soma = soma + num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

media = soma / 5

print(f"Soma dos números: {soma}")

print(f"Média dos números: {media}")

print(f"Maior número: {maior}")

print(f"Menor número: {menor}")