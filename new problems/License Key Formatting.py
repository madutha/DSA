def licenseKeyFormatting(s,k):
    s = s.replace("-", "").upper()

    first_group = len(s)% k or k
    groups = [s[:first_group]]
    for i in range(first_group,len(s),k):
        groups.append(s[i:i+k])

    return "-".join(groups)








s = "5F3Z-2e-9-w"
k = 4
print(licenseKeyFormatting(s,k))