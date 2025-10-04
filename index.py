from model import translate

def main():
    print("🌐 Mini Language Translator")
    print("Choose translation direction:")
    print("1. English → Hindi")
    print("2. Hindi → English")
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        direction = "en-hi"
        text = input("\nEnter English text: ")
    elif choice == "2":
        direction = "hi-en"
        text = input("\nEnter Hindi text: ")
    else:
        print("❌ Invalid choice. Exiting...")
        return

    print("\n🔄 Translating...")
    result = translate(text, direction)
    print("\n✅ Translation Result:")
    print(result)

if __name__ == "__main__":
    main()
