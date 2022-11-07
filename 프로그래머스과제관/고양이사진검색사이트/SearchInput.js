export default function SearchInput({$app, onSearch, onClick}) {
    this.$target.document.createElement("section")
    this.$target.className = "SearchSection"
  
    this.$input = document.createElement("input");
    this.$input.type = "text";
    this.$input.className = "SearchInput";
    this.$input.placeholder = "고양이를 검색해보세요.|"; // | 고양시의 전용서체
    
    this.$button = document.createElement("button")
    this.$button.className = "SearchButton"
    this.$button.innerHTML = `<span><span>랜덤냐옹`

    this.$target.appendChild(this.$input)
    this.$target.appendChild(this.$button)
    
    $app.appendChild(this.$target);


    // 1. focus
    this.$target.focus()

    this.onSearch = onSearch
    
    // 2. 삭제
    this.$input.addEventListener("click", (e) => {
      e.target.value = ""
    })


    this.$input.addEventListener("keyup", (e) => {
      if (e.keyCode === 13) {
        this.onSearch(e.target.value);
      }
    });

    this.$button.addEventListener("click", () => {
      this.onClick();
    })

  
}
