#!/usr/bin/env python
import optparse

# colors in cmd line. See - http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
class bcolors:
    IMPORTANT = '\033[01m'
    WARNING = '\033[93m'
    FAIL = '\033[01;93m'
    ENDC = '\033[0m'

    def disable(self):
        self.IMPORTANT = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
 
def main():
  p = optparse.OptionParser()
  p.add_option('--file', '-f', default="")
  p.add_option('--max-size', '-m', default='8000')
  p.add_option('--max-sram', '-s', default='1000')
  p.add_option('--warn-sram', '-w', default='0')
  options, arguments = p.parse_args()
  # init warn_sram size
  warn_sram = int(options.warn_sram)
  if (warn_sram == 0):
    warn_sram = int(int(options.max_sram) * 0.80);

  fyle = open(options.file)
  indx = 1
  sizes = {'.text' : 1, '.data' : 2, '.bss' : 3}  #dictionary (key/val array)
  for lyne in fyle :
    # Do string processing here
    if (indx == 1):
      fname = lyne[:len(lyne)-2]
    elif (indx == 2):
      # header line - do nothing
      dummy = 1
    elif (lyne[0] == '.'):
      # parse line
      tokens = lyne.split( )
      #print tokens
      #print "line: %s" % tokens[1]
      sizes[tokens[0]] = tokens[1]
    indx = indx + 1
  fyle.close()

  sketch_size = int(sizes['.text'])
  sram_size = int(sizes['.data']) + int(sizes['.bss'])

#  print 'Sketch file: %s' % fname
  print '--------'
#  print bcolors.IMPORTANT + "Memory Details:" + bcolors.ENDC
  print "Memory Details:"
  print "Binary sketch size: %s bytes (of %s bytes maximum); %s%% used" %(sketch_size, options.max_size, int(100 * sketch_size / float(options.max_size)))
  print "SRAM size: %s bytes (of %s bytes maximum); %s%% used" %(sram_size, options.max_sram, int(100 * sram_size / float(options.max_sram)))
  print '-------'


  if (sram_size > int(options.max_sram)):
    print bcolors.FAIL + "ERROR: Allowable chip memory exceeded." + bcolors.ENDC + " See http://www.arduino.cc/en/Reference/PROGMEM to reduce ram size"
  elif (sram_size > warn_sram):
    print bcolors.WARNING + "WARNING: Large amount of chip memory used."  + bcolors.ENDC +" Consider using PROGMEM, http://www.arduino.cc/en/Reference/PROGMEM, to reduce ram size"
    
  if (sketch_size > int(options.max_size)):
    print bcolors.FAIL + "ERROR: Sketch too big." + bcolors.ENDC + " See http://www.arduino.cc/en/Guide/Troubleshooting#size for tips on reducing it."

 
if __name__ == '__main__':
  main()



