//bin/true; rustc -o "/tmp/$0.bin" 1>&2 "$0" && "/tmp/$0.bin" "$@"; exit $?
fn main() {
    // let nx = 14066;

    // // let mut results: Vec<(i32, i32)> = vec![];
    // for i in 0..nx {
    //     for j in 0..nx {
    //         // results.push((j, i))

    //         println!("{},{}", j, i);
    //     }
    // }
    // // println!("{:#?}", results);

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
