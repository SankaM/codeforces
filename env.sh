# Source from repo root:  source env.sh
# Or add to ~/.zshrc:  source /Users/sanka/IdeaProjects/codeforces/env.sh
_cf_script="${BASH_SOURCE[0]:-$0}"
_CF_ROOT="$(cd "$(dirname "$_cf_script")" && pwd)"
export PATH="$_CF_ROOT/bin:$PATH"
