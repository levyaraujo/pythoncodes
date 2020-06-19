"Settings
let g:airline_powerline_fonts = 1

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif


"Enable the Airline Theme symbols

"Unicode Symbols
let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'

"Airline Symbols
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ''


"Personal Settings
set hidden
set mouse=a
set number  "Show the numbers of line
syntax on
set t_Co=256
set ts=4
set autoindent
set expandtab
set showmatch
let python_highlight_all = 1
set background=dark
colorscheme gruvbox
let g:airline_theme='gruvbox_material'
let mapleader = "\<space>" "Set the mapleader as SPACE KEY
nnoremap <leader>n <ESC>:NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'
nmap <F8> :TagbarToggle<CR>
nnoremap <leader>c :vs<CR>


"File searches
map <C-p> :Files<CR>



if !exists("g:jedi#auto_vim_configuration") || g:jedi#auto_vim_configuration
    " jedi-vim doesn't work in compatible mode (vim script syntax problems)
    if &compatible
        set nocompatible
    endif

    " jedi-vim really needs, otherwise jedi-vim cannot start.
    filetype plugin on

    " Change completeopt, but only if it has Vim's default value.
    let s:save_completeopt=&completeopt
    set completeopt&
    let s:default_completeopt=&completeopt
    let &completeopt=s:save_completeopt
    if s:default_completeopt == &completeopt
        set completeopt=menuone,longest,preview
    endif

    if len(mapcheck('<C-c>', 'i')) == 0
        inoremap <C-c> <ESC>
    endif
endif

" Pyimport command
command! -nargs=1 -complete=custom,jedi#py_import_completions Pyimport :call jedi#py_import(<q-args>)

command! -nargs=0 JediDebugInfo call jedi#debug_info()
command! -nargs=0 -bang JediClearCache call jedi#clear_cache(<bang>0)

"vim: set et ts=4:


"Insert Mode - change the block to line. Like this: | 
if has("autocmd")
  au VimEnter,InsertLeave * silent execute '!echo -ne "\e[1 q"' | redraw!
  au InsertEnter,InsertChange *
    \ if v:insertmode == 'i' | 
    \   silent execute '!echo -ne "\e[5 q"' | redraw! |
    \ elseif v:insertmode == 'r' |
    \   silent execute '!echo -ne "\e[3 q"' | redraw! |
    \ endif
  au VimLeave * silent execute '!echo -ne "\e[ q"' | redraw!
endif
"End of general settings

autocmd FileType python map <buffer> <F9> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F9> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>


"Plugins
call plug#begin('~/.vim/plugged')
"Themes
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'morhetz/gruvbox'
Plug 'scrooloose/nerdtree'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'sainnhe/gruvbox-material'
Plug 'jiangmiao/auto-pairs'

"Programming
Plug 'tpope/vim-fugitive'
Plug 'hdima/python-syntax'
Plug 'nvie/vim-flake8'
Plug 'pangloss/vim-javascript'
Plug 'davidhalter/jedi-vim'
Plug 'python-rope/ropevim'
Plug 'sheerun/vim-polyglot'
Plug 'tell-k/vim-autopep8'

"General Plugins
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all'  }
Plug 'junegunn/fzf.vim'
Plug 'majutsushi/tagbar'

call plug#end()