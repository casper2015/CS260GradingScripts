'''
Author: Mihir Rao
Purpose: Student List & Test cases for Programming Assignments for CS260 with Dr. Osmanlioglu
'''

student_id_list = [
  "abc123"
]

pa1_test_cases_dict = {
    "insertToHead john brown 1.76 35\ninsertToHead jonathan green 1.68 27\nprintList\nprintListInfo" : "[0]	jonathan	green	1.68	27\n[1]	john	brown	1.76	35\nsize:2, capacity:2\n",
    "insertToHead john brown 1.76 35\ninsertToHead jonathan green 1.68 27\ninsertToPosition 1 carolyn fusch 1.72 21\nprintList\nprintListInfo\nfindPosition carolyn\nfindPosition david" : "[0]	jonathan	green	1.68	27\n[1]	carolyn	fusch	1.72	21\n[2]	john	brown	1.76	35\nsize:3, capacity:4\n1\n-1\n",
    "insertToHead john brown 1.76 35\ninsertToHead jonathan green 1.68 27\ninsertToPosition 1 carolyn fusch 1.72 21\ninsertToPosition 3 david anderssonn 1.75 28\nprintList\nprintListInfo\nfindPosition david\ninsertToTail sylvia white 1.81 22\nprintList\nprintListInfo": "[0]	jonathan	green	1.68	27\n[1]	carolyn	fusch	1.72	21\n[2]	john	brown	1.76	35\n[3]	david	anderssonn	1.75	28\nsize:4, capacity:4\n3\n[0]	jonathan	green	1.68	27\n[1]	carolyn	fusch	1.72	21\n[2]	john	brown	1.76	35\n[3]	david	anderssonn	1.75	28\n[4]	sylvia	white	1.81	22\nsize:5, capacity:8\n",
    "insertToHead john brown 1.76 35\ninsertToHead jonathan green 1.68 27\ninsertToPosition 1 carolyn fusch 1.72 21\ninsertToPosition 3 david anderssonn 1.75 28\ninsertToTail sylvia white 1.81 22\nprintList\nprintListInfo\ndeleteFromHead\ndeleteFromTail\nprintList\nprintListInfo": "[0]	jonathan	green	1.68	27\n[1]	carolyn	fusch	1.72	21\n[2]	john	brown	1.76	35\n[3]	david	anderssonn	1.75	28\n[4]	sylvia	white	1.81	22\nsize:5, capacity:8\n[0]	carolyn	fusch	1.72	21\n[1]	john	brown	1.76	35\n[2]	david	anderssonn	1.75	28\nsize:3, capacity:4\n",
    "insertToHead john brown 1.76 35\ninsertToHead jonathan green 1.68 27\ninsertToPosition 1 carolyn fusch 1.72 21\ninsertToPosition 3 david anderssonn 1.75 28\ninsertToTail sylvia white 1.81 22\nprintList\nprintListInfo\ndeleteFromHead\ndeleteFromTail\ndeleteFromPosition 1\nprintList\nprintListInfo\ndeleteList" : "[0]	jonathan	green	1.68	27\n[1]	carolyn	fusch	1.72	21\n[2]	john	brown	1.76	35\n[3]	david	anderssonn	1.75	28\n[4]	sylvia	white	1.81	22\nsize:5, capacity:8\n[0]	carolyn	fusch	1.72	21\n[1]	david	anderssonn	1.75	28\nsize:2, capacity:4\n"
}
