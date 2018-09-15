# Life Signs
# Develop and test a program that determines  how many breaths and how many
# heartbeats a person has had in their life.
# The average respiration (breath) rate of people varies with age.

print('Life Signs')
age_user = int(input('Enter your age: '))

if age_user < 1:
    bpm = 60
elif age_user < 4:
    bpm = 30
elif age_user < 14:
    bpm = 25
elif age_user < 18 or age_user > 18:
    bpm = 23

minutes_lived = age_user * 365 * 24 * 60
seconds_lived = minutes_lived * 60
heart_rate = seconds_lived * seconds_lived
bpm_total = minutes_lived * bpm
print('your breaths per minute is: ', bpm, '\n'
, "You've lived for: ", format(minutes_lived,',.1f'),' minutes','\n'
,"Which means you've had: ",format(bpm_total,',.1f'),' breaths','\n'
,"The amount of times your heart has beaten is: ",format(heart_rate, ',.1f'),sep='')
