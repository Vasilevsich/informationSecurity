import mathRelated
import client
import server
n = mathRelated.generate_safe_prime(100, 200)
print('n is ', n)
g = mathRelated.calculate_primitive_root(n)
print('g is ', g)
k = 3
server = server.Server(n, g)
print('Server created')
# registration
client = client.Client(n, g, 'login', 'pass')
print('Client created')
server.add_user(client.send_reg_message())

a_message = client.generate_a()
b_message = server.generate_b(a_message)
print('Client session key is: ', client.generate_client_session_key(b_message))
print('Server session key is: ', server.generate_server_session_key('login'))
m_1 = client.generate_m_1()
server.compare_m_1(m_1)
