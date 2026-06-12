# game_loop.py - with retry and better error handling

player_state = {
    "xp": 0,
    "abilities": []
}

def test_double(user_code: str) -> tuple[bool, str]:
    """Return (passed, message)"""
    try:
        namespace = {}
        exec(user_code, namespace)
        if 'double' not in namespace:
            return False, "Your code doesn't define a function named 'double'."
        result = namespace['double'](5)
        if result == 10:
            return True, "✅ double(5) returned 10!"
        else:
            return False, f"❌ double(5) returned {result}, expected 10."
    except Exception as e:
        return False, f"❌ Code error: {e}"

def test_greet(user_code: str) -> tuple[bool, str]:
    try:
        namespace = {}
        exec(user_code, namespace)
        if 'greet' not in namespace:
            return False, "No 'greet' function found."
        result = namespace['greet']("Hero")
        if result == "Hello, Hero!":
            return True, "✅ greet('Hero') returned 'Hello, Hero!'"
        else:
            return False, f"❌ greet('Hero') returned {result}, expected 'Hello, Hero!'"
    except Exception as e:
        return False, f"❌ Code error: {e}"

quests = [
    {
        "title": "The Double Spell",
        "description": "Write a function 'double(x)' that returns x * 2.",
        "test_func": test_double,
        "xp_reward": 50,
        "ability_reward": "Basic Arithmetic"
    },
    {
        "title": "Greeting Ritual",
        "description": "Write a function 'greet(name)' that returns 'Hello, {name}!'",
        "test_func": test_greet,
        "xp_reward": 75,
        "ability_reward": "String Magic"
    }
]

print("⚔️ Welcome to DevArcana! ⚔️\n")

for idx, quest in enumerate(quests, 1):
    retries = 0
    max_retries = 2
    success = False
    
    while retries <= max_retries and not success:
        print(f"\n📜 Quest {idx}: {quest['title']} (Attempt {retries+1}/{max_retries+1})")
        print(quest['description'])
        print("Enter your Python code (blank line to finish):")
        
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        user_code = "\n".join(lines)
        
        if not user_code.strip():
            print("⚠️ You didn't enter any code. Try again.")
            retries += 1
            continue
        
        passed, message = quest["test_func"](user_code)
        print(message)
        
        if passed:
            player_state["xp"] += quest["xp_reward"]
            if quest["ability_reward"] not in player_state["abilities"]:
                player_state["abilities"].append(quest["ability_reward"])
            print(f"\n✨ Victory! +{quest['xp_reward']} XP")
            print(f"   Total XP: {player_state['xp']}")
            print(f"   Abilities: {', '.join(player_state['abilities'])}")
            success = True
        else:
            retries += 1
            if retries <= max_retries:
                print("💀 Try again! Fix your code.\n")
            else:
                print(f"\n💀 Quest failed after {max_retries+1} attempts. Game over.")
                break
    
    if not success:
        break
else:
    print("\n🏆 Congratulations! You completed all quests!")

print("\n🏁 Game session complete.")