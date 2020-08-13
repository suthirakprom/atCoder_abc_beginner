import 'dart:io';

void main() {
  var n = int.parse(stdin.readLineSync());
  var m = int.parse(stdin.readLineSync());  
  var listNum = new List(n);
  
  for(var i; i<n; i++) {
    listNum.add(m);
  }
  
  print(listNum);
}
