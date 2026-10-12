from main import text_to_morse

morse, unsupported = text_to_morse("SOS")

assert morse == "... --- ..."
assert unsupported == []

morse, unsupported = text_to_morse("HELLO WORLD")

assert morse == ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
assert unsupported == []

# Test lowercase input
morse, unsupported = text_to_morse("sos")
assert morse == "... --- ..."
assert unsupported == []

# Test numbers
morse, unsupported = text_to_morse("123")
assert morse == ".---- ..--- ...--"
assert unsupported == []

# Test unsupported characters
morse, unsupported = text_to_morse("HI@")
assert morse == ".... .."
assert unsupported == ["@"]

print("All tests passed!")