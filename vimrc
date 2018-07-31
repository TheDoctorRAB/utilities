set runtimepath+=~/.vim_runtime

source ~/.vim_runtime/vimrcs/basic.vim
source ~/.vim_runtime/vimrcs/filetypes.vim
source ~/.vim_runtime/vimrcs/plugins_config.vim
source ~/.vim_runtime/vimrcs/extended.vim
source ~/.vim_runtime/my_plugins/AutoSave.vim

try
source ~/.vim_runtime/my_configs.vim
catch
endtry

let g:auto_save = 1
set number
