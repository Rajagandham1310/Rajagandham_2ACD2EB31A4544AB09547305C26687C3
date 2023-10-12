def linearSearchProduct(productList,targetProduct):
  indices = []
  for index,product in enumerate (productList):
    if product==targetProduct:
     indices.append(index)
   
  return indices
  product =["shoes","boat","loafer","shoes","sadal","shoes"]
  target ="shoes"
  target2="apple"
  result =linearSearchProduct(products,target2)
  print(result)
 
   