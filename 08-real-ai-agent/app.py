from graph import graph


def main():
    print("=" * 50)
    print("🤖 Production AI Agent")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:
        user_input = input("\n👤 You: ")

        if user_input.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        state = {
            "messages": [],
            "user_input": user_input,
            "planner_output": None,
            "tool_output": "",
            "final_response": "",
            "error": "",
        }

        result = graph.invoke(state)

        print(f"\n🤖 AI: {result['final_response']}")


if __name__ == "__main__":
    main()