import base64

one="bmFtZT1ib2ImYWRtaW49RmFsc2U="
two="plrEGlOwYi0o+yBkQy8L/ta654ml4NrEx1XGLgSDZ10="

#bmFtZT0mYWRtaW49RmFsc2U=.5Gp5MsRyH22EkW8iqdRz2ulPfLzR72fuyXM7mgIyGEc=

one="bmFtZT0mYWRtaW49RmFsc2U="
two="5Gp5MsRyH22EkW8iqdRz2ulPfLzR72fuyXM7mgIyGEc="
print(base64.b64encode(b'name=&admin=False'))
# print(base64.b64decode(one))
print(base64.b64decode(two).hex())