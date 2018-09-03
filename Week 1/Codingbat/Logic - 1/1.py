def cigar_party(cigars, is_weekend):
  if(40<=cigars<=60 or (is_weekend and 40<=cigars)):
    return True
  return False
