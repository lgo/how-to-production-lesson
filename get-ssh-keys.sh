#!/bin/bash
users="andyzg tarateesang jmagbits jefferyyli kevnchan NareshAnadkat kaitlynyong kathyrinelu thekevlau kartiktalwar snario aciliana theroughcode GautamGupta matteogp baijerry DChang87 shelaq Imtizzle meagan-furgal Jenevievea  iriswen joanna-chen moezbhatti kashishgoel yulihav ioanacrant corbin737 kpsuperplane xlegoz moaazsidat darrenlii m2iyer zipatel carol-yao jennynotjen jacobwills"
rm keys
touch keys
for user in $users; do
  echo "Getting $user"
  echo "# $user" >> keys
  curl https://github.com/$user.keys >> keys 2>/dev/null
done

echo "Done"
