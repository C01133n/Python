infile=open('InputToFile1.txt','rt')
outfile=open('jolly.txt','wt')
print( 'processing input')
sum=''
for line in infile:
    sum+=str(line)
    print( line.rstrip(),file=outfile)
print('\nResults: '+str(sum),file=outfile)
outfile.close()
print('Output Complete')
    