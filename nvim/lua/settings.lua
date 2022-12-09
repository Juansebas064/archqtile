-- Neovim API aliases
local cmd = vim.cmd
local exec = vim.api.nvim_exec
local fn = vim.fn
local g = vim.g
local opt = vim.opt

-- General
g.mapleader = " "

-- UI
opt.number = true
--opt.relativenumber = true
opt.ignorecase = true
opt.smartcase = true
opt.hlsearch = false
opt.wrap = true
opt.breakindent = true
opt.sw = 2
opt.expandtab = false
opt.syntax = enable
opt.showmatch = true
opt.termguicolors = true
cmd("colorscheme spacegray")
