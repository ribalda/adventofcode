#include <stdio.h>
#include <stdint.h>

void add_num(int64_t n)
{
  static int64_t values[20000];
  static int idx = 0;
  int i;
  for (i = 0; i < idx; i++)
    if (values[i] == n)
      return;
  fprintf(stdout, "%ld, %d\n", n, i);
  values[idx++] = n;
}

int main()
{
  int64_t c = 0, d = 0, e = 0;

  e = 0x7b;
aa:
  e = e & 0x1c8;
  if (e != 0x48)
    goto aa;
  e = 0x0;
bb:
  d = e | 0x10000;
  e = 0xc154d6;
cc:
  e = e & 0xffffff;
  e = (e + (d & 0xff)) * 0x1016b;
  e = e & 0xffffff;
  if (0x100 > d)
  {
    add_num(e);
    goto bb;
  }
  c = 0x0;
dd:
  if (((c + 1) * 0x100) > d)
  {
    d = c;
    goto cc;
  }
  c = c + 0x1;
  goto dd;
}