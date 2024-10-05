# AWK

AWK is a domain-specific language designed for text processing and typically used as a data extraction and reporting tool. Like sed and grep, it is a filter, and is a standard feature of most Unix-like operating systems.

<details>
<summary>Usage</summary>

```sh
gawk -f script.awk INPUT_FILE.csv
```

When script.awk contents
>BEGIN {FS="|"; OFS="|"}
{
if ( ( $4 == "TEXT1" || $4 == "TEXT1b" ) && ( $2 != "NOT_TEXT" || $2 != "NOT_TEXT2" ) ){
        $1 = "REPLACE_VALUE_IN_COL1";
        $3 = "TELEFONIA MOVIL";
        $5 = "2000";
        print;
}


</details>