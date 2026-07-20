from workflow import graph

result = graph.invoke(
    {
        "topic": "Artificial Intelligence in Healthcare"
    }
)

print("\n" + "=" * 70)
print("FINAL REPORT")
print("=" * 70)
print()

print(result["final_report"])