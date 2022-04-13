import math
from error_calc import Rules

mu_naut = 4 * math.pi * 10**-7 # Tm/A

def magnetic_field(N:int, I:list, r:float):
	B_c = []
	for i in I:
		B_c.append((mu_naut * (i / 1000) * N) / (2 * r))
	return B_c

def tangent(theta:list):
	tan_theta = []
	for i in theta:
		tan_theta.append(math.tan(i))
	return tan_theta

def earth_magnetic(B_c:list, tan_theta:list):
	B_e = []
	for i in range(len(B_c)):
		B_e.append(B_c[i] / tan_theta[i])
	return sum(B_e) / len(B_e)

def m_to_base(convert:list):
	return_list = []
	for i in convert:
		return_list.append(i / 1000)
	return return_list

if __name__ == '__main__':

	radius = 0.1125 # m

	N_1 = 100

	theta_1 = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]
	I_1 = [-4.5, -12.3, -17.1, -27.9, -45, 4.2, 13.3, 19.8, 30.4, 40.9]

	B_c_1 = magnetic_field(N_1, I_1, radius)
	tan_theta_1 = tangent(theta_1)

	N_2 = 300

	theta_2 = [10, 20, 30, 40, 50, -10, -20, -30, -40, -50]
	I_2 = [-1.2, -4.2, -6.1, -9.3, -14.4, 2.2, 4, 6.7, 9.6, 14.7]

	B_c_2 = magnetic_field(N_2, I_2, radius)
	tan_theta_2 = tangent(theta_2)

	print(f'B_c 1: {B_c_1}')
	print(f'tan_theta 1: {tangent(theta_1)}')
	print(m_to_base(I_1))

	print(f'B_c 2: {B_c_2}')
	print(f'tan_theta 2: {tangent(theta_2)}')
	print(m_to_base(I_2))

	print(earth_magnetic(B_c_1, tan_theta_1))
	print(earth_magnetic(B_c_2, tan_theta_2))

	error_tan_theta = math.tan(1)
	error_I = 0.1 / 1000
	error_r = 0.001

	values_1 = [(sum(m_to_base(I_1)) / len(I_1)), N_1, (sum(tan_theta_1) / len(tan_theta_1)), radius]
	values_2 = [(sum(m_to_base(I_2)) / len(I_2)), N_2, (sum(tan_theta_2) / len(tan_theta_2)), radius]
	errors = [error_I, 0, error_tan_theta, error_r]
	exponents = [1, 1, 1, 1]
	q_1 = 1.949222205158665e-05
	q_2 = 1.960864003838236e-05

	print(Rules.rule4(values_1, errors, exponents, q_1))
	print(Rules.rule4(values_2, errors, exponents, q_2))
