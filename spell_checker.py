# Spell Checker using Minimum Edit Distance

# Function to calculate edit distance
def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Create matrix
    dp = [[0 for x in range(n + 1)] for y in range(m + 1)]

    # Fill first row and column
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    # Fill remaining cells
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost  # Replacement
            )

    return dp[m][n]


# Load dictionary words
with open("dictionary.txt", "r") as file:
    dictionary = file.read().splitlines()

# User input
user_word = input("Enter a word: ").lower()

# Check exact match
if user_word in dictionary:
    print("Correct spelling!")
else:
    min_distance = float('inf')
    suggestion = ""

    # Find closest word
    for word in dictionary:
        distance = edit_distance(user_word, word)

        if distance < min_distance:
            min_distance = distance
            suggestion = word

    print("Incorrect spelling!")
    print("Did you mean:", suggestion, "?")