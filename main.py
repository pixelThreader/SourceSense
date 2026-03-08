"""Executable entrypoint for running SourceSense end-to-end.

This script provides sample source paragraphs, runs the core SourceSense
pipeline, and renders consensus results in the terminal dashboard.
"""

from src.core.orchestrator import run_sourcesense
from src.tui.dashboard import show_results


paragraphs = [
    """
Rust is often praised for its strong memory safety guarantees. The language uses an ownership and borrowing system that prevents common bugs such as use-after-free and data races. Many systems programmers claim that these guarantees allow developers to build reliable low-level software without relying on a garbage collector.

Some developers argue that Rust significantly improves software reliability in systems programming. They say the strict compile-time checks help prevent entire classes of runtime crashes. Because of this, companies building infrastructure software increasingly consider Rust for new components.

C++ has historically dominated systems programming because it offers direct control over memory and hardware resources. Developers can manually allocate and free memory, which allows highly optimized performance. However, this flexibility also increases the risk of memory corruption bugs.

Critics of Rust claim that the language does not eliminate all memory errors. They argue that logical bugs and unsafe code blocks can still introduce vulnerabilities. According to these critics, Rust improves safety but cannot guarantee perfectly secure software.

Several large technology companies have started experimenting with Rust for critical infrastructure services. They report that Rust reduces the frequency of memory safety bugs compared to traditional C or C++ codebases. These companies also note that Rust's compiler catches mistakes earlier in development.

Some engineers believe that Rust's ownership model makes the language harder to learn for beginners. The borrow checker introduces concepts that many developers have never encountered before. As a result, new Rust programmers sometimes struggle with the language's strict rules.

Proponents of Rust argue that the learning curve pays off in the long run. Once developers understand the ownership model, they often write safer and more maintainable code. Rust programs may require more thought during development but tend to produce fewer runtime errors.

In contrast, some programmers say that C++ provides more flexibility than Rust. Because C++ allows unrestricted pointer manipulation, developers can implement highly specialized optimizations. This flexibility is sometimes necessary for performance-critical systems.

Security researchers frequently point out that memory safety issues are a major cause of software vulnerabilities. Buffer overflows, dangling pointers, and use-after-free errors appear regularly in C and C++ applications. Rust was designed specifically to reduce these types of vulnerabilities.

However, not everyone agrees that Rust is always the best solution for secure systems. Some engineers argue that well-written C++ code can also be safe if developers follow strict coding standards. They claim that disciplined programming practices can mitigate many traditional memory risks.

Modern operating system projects have started experimenting with Rust modules. For example, certain kernel components are being rewritten in Rust to improve reliability. Developers hope that these components will reduce the number of security vulnerabilities discovered in kernel code.

There are also concerns that Rust compilation times can be slower than those of C++. Large Rust projects sometimes take longer to compile due to extensive compile-time analysis. Developers occasionally complain that these slower build times reduce productivity.

Many developers highlight Rust's strong concurrency model as one of its biggest advantages. The language prevents data races at compile time through its ownership rules. This design allows developers to write parallel programs without many of the traditional synchronization bugs.

Skeptics argue that Rust's strict type system can sometimes feel overly restrictive. They say the compiler occasionally rejects code that would actually run safely. These developers prefer languages that allow more freedom even if it increases risk.

Several performance benchmarks suggest that Rust programs can match the speed of C++ programs. Because Rust does not require a garbage collector, it avoids the runtime overhead common in managed languages. This makes Rust suitable for performance-sensitive systems.

Some legacy system maintainers are hesitant to adopt Rust. They argue that rewriting large C or C++ codebases would require enormous effort. For these teams, the cost of migration may outweigh the potential safety benefits.

Open source communities have increasingly embraced Rust in recent years. Many new command-line tools and infrastructure utilities are written entirely in Rust. Developers appreciate the combination of performance, safety, and modern tooling.

Despite Rust's advantages, the ecosystem is still smaller than the long-established C++ ecosystem. Certain specialized libraries and frameworks are more mature in C++. This can make Rust adoption more challenging in some domains.

Advocates of Rust claim that the language represents the future of systems programming. They believe the industry will gradually move toward safer languages that reduce memory vulnerabilities. Rust is often presented as the leading candidate for this transition.

Others believe that C++ will remain important for decades because of its enormous existing codebase. Many critical systems already rely on C++ and cannot easily be replaced. For this reason, some engineers expect Rust and C++ to coexist rather than compete directly.
""",
]


def main():
    """Run SourceSense on bundled sample paragraphs and display results."""
    results, stats = run_sourcesense(paragraphs)
    show_results(results, stats)


if __name__ == "__main__":
    main()
