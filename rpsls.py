#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����ΰ
���ڣ�2020.4.8
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	# ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
	# ��Ҫ���Ƿ��ؽ��
	if   name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="ֽ":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4
	
def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""

	# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
	# ��Ҫ���Ƿ��ؽ��
	if   number==0:
		return "ʯͷ"
	elif number==1:
		return "ʷ����"
	elif number==2:
		return "ֽ"
	elif number==3:
		return "����"
	elif number==4:
		return "����"

def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

	"""


	# ���"-------- "���зָ�
	# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

	# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

	# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

	# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

	# ����Ļ����ʾ�����ѡ����������

	# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

	# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
	print("----------------")
	print("���ѡ��Ϊ:%s"%(player_choice))
	player_choice_number=name_to_number(player_choice)
	cope_number=random.randrange(0,4)
	cope_name=number_to_name(cope_number)
	print("�������ѡ��Ϊ��%s"%(cope_name))
	if   cope_number==player_choice_number:
		return "��ͼ��������һ����"
	elif cope_number==0 and (player_choice_number==3 or player_choice_number==4):
		return "����Ӯ�ˣ�"
	elif cope_number==1 and (player_choice_number==0 or player_choice_number==4):
		return "����Ӯ��"
	elif cope_number==2 and (player_choice_number==1 or player_choice_number==0):
		return "����Ӯ��"
	elif cope_number==3 and (player_choice_number==1 or player_choice_number==2):
		return "����Ӯ��"
	elif cope_number==4 and (player_choice_number==2 or player_choice_number==3):
		return "����Ӯ��"
	elif player_choice_number==0 and (cope_number==3 or cope_number==4):
		return "��Ӯ��"
	elif player_choice_number==1 and (cope_number==0 or cope_number==4):
		return "��Ӯ��"
	elif player_choice_number==2 and (cope_number==0 or cope_number==1):
		return "��Ӯ��"
	elif player_choice_number==3 and (cope_number==1 or cope_number==2):
		return "��Ӯ��"
	elif player_choice_number==4 and (cope_number==2 or cope_number==3):
		return "��Ӯ��"
	else:
		return "Error:No Correct Name"


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
print(rpsls(choice_name))


