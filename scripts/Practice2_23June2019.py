### Converter

#-----------------------------------------------------------------------------------

# kilometers to miles converter
kilometers_to_miles = 0.621

# miles to kilometer converter
miles_to_kilometers = 1.609

# feet to kilometers converter
feet_to_kilometers = 0.0003

# kilometers to feet converter
kilometers_to_feet = 3280.84


# feet to miles converter
feet_to_miles = 0.0002

# miles to feet converter
miles_to_feet = 5280


#-----------------------------------------------------------------------------------

input_unit = input("Input Unit - km or mi or ft...")
input_value = float(input("Value"))
output_unit = input("Output Unit - km or mi or ft...")
output_value = 0.0


if(input_unit=="km" and output_unit =="mi"):
    output_value = input_value*kilometers_to_miles

elif(input_unit=="mi" and output_unit =="km"):
    output_value = input_value*miles_to_kilometers

elif(input_unit=="ft" and output_unit =="km"):
    output_value = input_value*feet_to_kilometers

elif(input_unit=="km" and output_unit =="ft"):
    output_value = input_value*kilometers_to_feet

elif(input_unit=="ft" and output_unit =="mi"):
    output_value = input_value*feet_to_miles

elif(input_unit=="mi" and output_unit =="ft"):
    output_value = input_value*feet_to_miles

else:
    print("Enter Correct Units")

print(str(input_value)+" "+input_unit+" equals "+str(output_value)+" " +output_unit)
