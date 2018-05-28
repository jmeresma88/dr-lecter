train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = ((f_temp)-32)*5/9
  return c_temp

f100_in_celsius = f_to_c(100)

#prints 100 degrees fahrenheit in celsius
print("{:.1f}".format(f100_in_celsius))

def c_to_f(c_temp):
  f_temp = (c_temp)*(9/5)+32
  return f_temp

c0_in_fahrenheit = c_to_f(0)

#prints 0 degrees celsius in fahrenheit
print("{:.1f}".format(c0_in_fahrenheit))

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

train_force = get_force(train_mass, train_acceleration)

print("{:,}".format(train_force))

def get_energy(mass, c=3*10**8):
  energy = mass * c**2
  return energy

bomb_energy = get_energy(bomb_mass)

print("{:,}".format(bomb_energy))

def get_work(mass, acceleration, distance):
  work = (get_force(mass,acceleration))*distance
  return work

train_work = get_work(train_mass,train_acceleration,train_distance)

print("{:,}".format(train_work))

print("The GE train does "+str("{:,}".format(train_work))+" Joules of work over "+str(train_distance)+" meters.")

  

