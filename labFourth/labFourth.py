import mathRelated
import client
import server
n = mathRelated.generate_safe_prime(100, 200)
print('Safe prime is ', n)
g = mathRelated.calculate_primitive_root(n)
print('Generator is ', g)
k = 3
print('k is', k)
server = server.Server(n, g)
print('Server created')
# registration
client = client.Client(n, g, 'login', 'pass')
print('Client created')
print(f'Login: {client.username}, password: {client.password}')
server.add_user(client.send_reg_message())
print("Client's x is: ", client.x)
print('Client added to server')
a_message = client.generate_a()
print('Client generated A: ', a_message[1])
b_message = server.generate_b(a_message)
print('Server generated B: ', b_message[0])
print('Client generated session key: ', client.generate_client_session_key(b_message))
print('Server generated session key: ', server.generate_server_session_key('login'))
m_1 = client.generate_m_1()
server.compare_m_1(m_1)
