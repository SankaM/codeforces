plugins {
    application
    java
}

val cfProblemDir: String =
    (project.findProperty("cf.problem.dir") as String?) ?: "contests/_bootstrap/A"

val cfStdinPath: String =
    (project.findProperty("cf.stdin") as String?) ?: "samples/001.in"

layout.projectDirectory.file(cfProblemDir).asFile.let { dir ->
    require(dir.isDirectory) {
        "cf.problem.dir points to missing folder: ${dir.path} — run ./bin/cf init ... or ./bin/cf use ..."
    }
}

sourceSets {
    named("main") {
        java.setSrcDirs(listOf(file(cfProblemDir)))
    }
}

application {
    mainClass.set("Main")
}

tasks.named<JavaExec>("run") {
    val dir = file(cfProblemDir)
    val stdin = File(dir, cfStdinPath)
    if (stdin.isFile) {
        standardInput = stdin.inputStream()
    }
}

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(17))
    }
}
