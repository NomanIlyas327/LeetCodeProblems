# Isay aam tor par "Needle in a Haystack" kehte hain.

# Asaan Matlab:
# Aapko do strings di jati hain: ek bari string (haystack) aur ek choti string (needle). Aapko batana hai ke choti string, bari string mein sab se pehli baar kahan aati hai uska index (0, 1, 2...) return karna hai. Agar nahi milti to -1 return karna hai.

# Misaal (Example):

# Haystack: "hello"

# Needle: "ll"

# Jawab: 2 (Kyunke "ll" index 2 se shuru ho raha hai).

# Samajhne ka Tariqa (Logic):

# Window Sliding: Aap bari string ke har character par jaatay hain aur wahan se check karte hain ke kya aglay characters "needle" ke barabar hain?

# Optimization: Agar needle ki lambayi 5 hai, to aapko bari string ke aakhri 4 characters check karne ki zaroorat nahi, kyunke wahan 5-character ki needle poori aa hi nahi sakti.

haystack = "Pakistan"
needle = "stan"
m = len(haystack)    
print(m)
n = len(needle)
print(n)
def strStr(haystack, needle):
    if n == 0:
        return 0
    for i in range(m - n + 1):
        if haystack[i:i + n] == needle:
            return i
    return -1
print(strStr(haystack, needle))
