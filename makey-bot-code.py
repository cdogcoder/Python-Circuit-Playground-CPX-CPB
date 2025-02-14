makey_bot_dict = {
  "wave_pattern": [90, 1.5, 45, 2.3, 78, 3.4],
  "eyes_rgb_status": 1,
  "rgb_eye_color_1": "#44014f",
  "rgb_eye_color_2": "#7fa0b9",
  "7seg_value": 5,
  "led_1_status": 1,
  "led_1_blink": 3.0,
  "led_2_status": 0,
  "led_2_blink": 2.5,
  "led_3_status": 1,
  "led_3_blink": 1.7
}

def printOutDictionary(dictionary):
  for key in dictionary.keys():
    print(key, dictionary[key])

printOutDictionary(makey_bot_dict)

user_input = input("Enter a key name: ")
if user_input in makey_bot_dict.keys():
  user_input2 = input("Enter a value to update the key with: ")
  makey_bot_dict[user_input] = user_input2
  print(user_input, ":", makey_bot_dict[user_input])
else:
  print("Not in dictionary")
