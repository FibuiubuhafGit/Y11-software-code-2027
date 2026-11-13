pack1 = float(input('Cost of packet 1? '))
pack1b = int(input('Biscuits in packet 1? '))

pack2 = float(input('Cost of packet 2? '))
pack2b = int(input('Biscuits in packet 2? ' ))

value1 = pack1b/pack1
value2 = pack2b/pack2

if value1 > value2:
    print('Packet 1')
elif value2 > value1:
    print('Packet 2')
elif value1 == value2:
    print("Packet 1 or 2")
