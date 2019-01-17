import copy

# Shallow copy is used to copy the reference pointers.
# These references point to the original objects and the changes made in the copy will also affect the original copy of it.
# Shallow copy allows faster execution of the program and it depends on the size of the data that is used.

# Deep copy doesn’t copy the reference pointers.
# In case of deep copy, a copy of object is copied in other object.
# It means that any changes made to a copy of object do not reflect in the original object.

motor_cycles = ['Royal Enfield', ['Avenger', 'Harley']]
motor_cycles_sc = copy.copy(motor_cycles)
motor_cycles_dc = copy.deepcopy(motor_cycles)

print("Elements in the original list before deep copy: {}".format(motor_cycles))
print("---------------------------------------------------------------------")

motor_cycles_dc[1][1] = 'BMW'
print("Elements in the deep copy: {}".format(motor_cycles_dc))
print("Elements in the original list after deep copy: {}".format(motor_cycles))
print("---------------------------------------------------------------------")

motor_cycles_sc[1][1] = 'Honda'
print("Elements in the shallow copy: {}".format(motor_cycles_sc))
print("Elements in the original list after shallow copy: {}".format(motor_cycles))
print("---------------------------------------------------------------------")