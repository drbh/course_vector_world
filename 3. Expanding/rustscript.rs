//bin/true; rustc -o "/tmp/$0.bin" 1>&2 "$0" && "/tmp/$0.bin" "$@"; exit $?
fn main() {
    let n = 14066;
    let mut m = 0;

    loop {
        for i in (m + 1)..n {
            println!("{:?},{:?}", i, m);
        }
        m = m + 1;

        if m == n {
            break;
        }
    }
}
